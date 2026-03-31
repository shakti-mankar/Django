import { useNavigate } from "react-router-dom";

const PaymentFailure = () => {
  const navigate = useNavigate();
  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.icon}>❌</div>
        <h2 style={styles.title}>Payment Failed</h2>
        <p style={styles.sub}>Something went wrong. Please try again.</p>
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
  sub:       { color:"#666", marginBottom:"20px" },
  btn:       { padding:"12px 32px", background:"#1a1a2e", color:"#fff",
               border:"none", borderRadius:"8px", fontSize:"15px", cursor:"pointer" },
};

export default PaymentFailure;