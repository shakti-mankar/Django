import { Link, useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("user"));

  const logout = () => {
    localStorage.removeItem("user");
    alert("Logout successful");
    navigate("/login");
  };

  return (
    <div style={{display:"flex",justifyContent:"space-between",padding:"15px",background:"#222",color:"white"}}>
      <h2>Job Portal</h2>

      <div>
        {!user && <Link to="/login" style={{marginRight:"10px",color:"white"}}>Login</Link>}
        {!user && <Link to="/register" style={{color:"white"}}>Register</Link>}
        {user && <button onClick={logout}>Logout</button>}
      </div>
    </div>
  );
};

export default Navbar;