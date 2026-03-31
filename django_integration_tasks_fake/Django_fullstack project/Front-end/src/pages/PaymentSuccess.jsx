import { useLocation, useNavigate } from "react-router-dom";

const PaymentSuccess = () => {
  const { state }  = useLocation();
  const navigate   = useNavigate();

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.icon}>✅</div>
        <h2 style={styles.title}>Payment Successful!</h2>
        <p style={styles.sub}>Thank you for your purchase.</p>
        {state?.payment_id && (
          <p style={styles.meta}>
            Payment ID: <strong>{state.payment_id}</strong>
          </p>
        )}
        {state?.product && (
          <p style={styles.meta}>
            Product: <strong>{state.product.name}</strong>
          </p>
        )}
        <button onClick={() => navigate("/dashboard")} style={styles.btn}>
          Back to Dashboard
        </button>
      </div>
    </div>
  );
};

const styles = {
  container: { minHeight:"100vh", display:"flex", alignItems:"center",
               justifyContent:"center", background:"#f0f2f5" },
  card:      { background:"#fff", padding:"48px", borderRadius:"12px",
               boxShadow:"0 4px 20px rgba(0,0,0,0.1)", textAlign:"center", maxWidth:"420px" },
  icon:      { fontSize:"56px", marginBottom:"16px" },
  title:     { color:"#1a1a2e", marginBottom:"8px" },
  sub:       { color:"#666", marginBottom:"16px" },
  meta:      { background:"#f9f9f9", padding:"10px", borderRadius:"8px",
               fontSize:"14px", marginBottom:"8px" },
  btn:       { marginTop:"20px", padding:"12px 32px", background:"#e94560",
               color:"#fff", border:"none", borderRadius:"8px",
               fontSize:"15px", cursor:"pointer" },
};

export default PaymentSuccess;