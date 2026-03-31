import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import API from "../api/axios";

const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [form, setForm] = useState({ username:"", password:"" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      const { data } = await API.post("/users/login/", form);
      login(data.user, data.access, data.refresh);
      navigate("/dashboard");
    } catch {
      setError("Invalid username or password.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2 style={styles.title}>Welcome Back 👋</h2>
        {error && <p style={styles.error}>{error}</p>}
        <form onSubmit={handleSubmit}>
          {["username", "password"].map((field) => (
            <input
              key={field}
              name={field}
              type={field === "password" ? "password" : "text"}
              placeholder={field.charAt(0).toUpperCase() + field.slice(1)}
              value={form[field]}
              onChange={handleChange}
              style={styles.input}
              required
            />
          ))}
          <button type="submit" style={styles.btn} disabled={loading}>
            {loading ? "Logging in..." : "Login"}
          </button>
        </form>
        <p style={styles.footer}>
          Don't have an account? <Link to="/signup">Sign Up</Link>
        </p>
      </div>
    </div>
  );
};

const styles = {
  container: { minHeight:"100vh", display:"flex", alignItems:"center",
               justifyContent:"center", background:"#f0f2f5" },
  card:      { background:"#fff", padding:"40px", borderRadius:"12px",
               boxShadow:"0 4px 20px rgba(0,0,0,0.1)", width:"100%", maxWidth:"400px" },
  title:     { textAlign:"center", marginBottom:"24px", color:"#1a1a2e" },
  input:     { width:"100%", padding:"12px", marginBottom:"16px", borderRadius:"8px",
               border:"1px solid #ddd", fontSize:"14px", boxSizing:"border-box" },
  btn:       { width:"100%", padding:"12px", background:"#1a1a2e", color:"#fff",
               border:"none", borderRadius:"8px", fontSize:"16px", cursor:"pointer" },
  error:     { color:"red", marginBottom:"12px", fontSize:"14px" },
  footer:    { textAlign:"center", marginTop:"16px", fontSize:"14px" },
};

export default Login;