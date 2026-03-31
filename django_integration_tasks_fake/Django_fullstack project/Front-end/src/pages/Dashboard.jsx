import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/axios";

const Dashboard = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading]   = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    API.get("/products/")
      .then(({ data }) => setProducts(data))
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p style={{ textAlign:"center", marginTop:"60px" }}>Loading products...</p>;

  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>🛍️ Available Products</h2>
      <div style={styles.grid}>
        {products.map((product) => (
          <div key={product.id} style={styles.card}>
            <h3 style={styles.name}>{product.name}</h3>
            <p style={styles.desc}>{product.description}</p>
            <p style={styles.price}>₹ {product.price}</p>
            <button
              style={styles.btn}
              onClick={() => navigate("/checkout", { state: { product } })}
            >
              Buy Now
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

const styles = {
  container: { padding:"32px", maxWidth:"1100px", margin:"0 auto" },
  heading:   { marginBottom:"24px", color:"#1a1a2e" },
  grid:      { display:"grid", gridTemplateColumns:"repeat(auto-fill, minmax(260px, 1fr))", gap:"24px" },
  card:      { background:"#fff", borderRadius:"12px", padding:"24px",
               boxShadow:"0 2px 12px rgba(0,0,0,0.08)" },
  name:      { fontSize:"18px", fontWeight:"bold", color:"#1a1a2e" },
  desc:      { color:"#666", fontSize:"14px", margin:"8px 0 16px" },
  price:     { fontSize:"22px", fontWeight:"bold", color:"#e94560", marginBottom:"16px" },
  btn:       { width:"100%", padding:"12px", background:"#e94560", color:"#fff",
               border:"none", borderRadius:"8px", fontSize:"15px", cursor:"pointer" },
};

export default Dashboard;