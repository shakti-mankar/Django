import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <nav style={styles.nav}>
      <Link to="/dashboard" style={styles.brand}>🛒 PayApp</Link>
      <div style={styles.links}>
        {user ? (
          <>
            <span style={styles.welcome}>👋 {user.username}</span>
            <button onClick={handleLogout} style={styles.btn}>Logout</button>
          </>
        ) : (
          <>
            <Link to="/login" style={styles.link}>Login</Link>
            <Link to="/signup" style={styles.link}>Signup</Link>
          </>
        )}
      </div>
    </nav>
  );
};

const styles = {
  nav:     { display:"flex", justifyContent:"space-between", alignItems:"center",
             padding:"12px 24px", background:"#1a1a2e", color:"#fff" },
  brand:   { color:"#e94560", fontWeight:"bold", fontSize:"20px", textDecoration:"none" },
  links:   { display:"flex", gap:"16px", alignItems:"center" },
  link:    { color:"#fff", textDecoration:"none" },
  welcome: { color:"#aaa", fontSize:"14px" },
  btn:     { background:"#e94560", color:"#fff", border:"none",
             padding:"8px 16px", borderRadius:"6px", cursor:"pointer" },
};

export default Navbar;