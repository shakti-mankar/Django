import { useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import API from "../api/axios";

const loadRazorpayScript = () =>
  new Promise((resolve) => {
    const script = document.createElement("script");
    script.src = "https://checkout.razorpay.com/v1/checkout.js";
    script.onload = () => resolve(true);
    script.onerror = () => resolve(false);
    document.body.appendChild(script);
  });

const Checkout = () => {
  const { state }  = useLocation();
  const { user }   = useAuth();
  const navigate   = useNavigate();
  const product    = state?.product;

  if (!product) {
    navigate("/dashboard");
    return null;
  }

  const handlePayment = async () => {
    const loaded = await loadRazorpayScript();
    if (!loaded) {
      alert("Failed to load Razorpay SDK. Check your internet connection.");
      return;
    }

    try {
      // Step 1: Create order on backend
      const { data: order } = await API.post("/payments/create-order/", {
        product_id: product.id,
      });

      // Step 2: Open Razorpay popup
      const options = {
        key:         order.key,
        amount:      order.amount,
        currency:    order.currency,
        name:        "PayApp",
        description: order.product_name,
        order_id:    order.order_id,
        prefill: {
          name:  user?.username,
          email: user?.email,
        },
        theme: { color: "#e94560" },

        handler: async (response) => {
          // Step 3: Verify payment on backend
          try {
            await API.post("/payments/verify/", {
              razorpay_order_id:   response.razorpay_order_id,
              razorpay_payment_id: response.razorpay_payment_id,
              razorpay_signature:  response.razorpay_signature,
            });
            navigate("/payment-success", {
              state: { payment_id: response.razorpay_payment_id, product }
            });
          } catch {
            navigate("/payment-failure");
          }
        },

        modal: {
          ondismiss: () => console.log("Payment popup closed."),
        },
      };

      const rzp = new window.Razorpay(options);
      rzp.open();

    } catch (err) {
      console.error("Order creation failed:", err);
      alert("Could not initiate payment. Please try again.");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2 style={styles.title}>Order Summary</h2>
        <div style={styles.row}>
          <span>Product</span>
          <strong>{product.name}</strong>
        </div>
        <div style={styles.row}>
          <span>Description</span>
          <span style={{ color:"#666", fontSize:"14px" }}>{product.description}</span>
        </div>
        <div style={styles.row}>
          <span>Amount</span>
          <strong style={{ color:"#e94560", fontSize:"20px" }}>₹ {product.price}</strong>
        </div>
        <hr style={{ margin:"20px 0", borderColor:"#eee" }} />
        <button onClick={handlePayment} style={styles.btn}>
          💳 Pay with Razorpay
        </button>
        <button onClick={() => navigate("/dashboard")} style={styles.backBtn}>
          ← Back to Products
        </button>
      </div>
    </div>
  );
};

const styles = {
  container: { minHeight:"100vh", display:"flex", alignItems:"center",
               justifyContent:"center", background:"#f0f2f5" },
  card:      { background:"#fff", padding:"40px", borderRadius:"12px",
               boxShadow:"0 4px 20px rgba(0,0,0,0.1)", width:"100%", maxWidth:"460px" },
  title:     { marginBottom:"24px", color:"#1a1a2e" },
  row:       { display:"flex", justifyContent:"space-between",
               alignItems:"center", marginBottom:"16px" },
  btn:       { width:"100%", padding:"14px", background:"#e94560", color:"#fff",
               border:"none", borderRadius:"8px", fontSize:"16px",
               cursor:"pointer", marginBottom:"12px" },
  backBtn:   { width:"100%", padding:"12px", background:"transparent", color:"#666",
               border:"1px solid #ddd", borderRadius:"8px",
               fontSize:"14px", cursor:"pointer" },
};

export default Checkout;