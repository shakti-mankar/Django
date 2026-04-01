// import { useState } from "react";
// import axios from "axios";
// import { useNavigate } from "react-router-dom";

// const Login = () => {
//   const [form, setForm] = useState({
//     email: "",
//     password: ""
//   });

//   const navigate = useNavigate();

//   const handleLogin = async (e) => {
//     e.preventDefault();

//     const res = await axios.get("http://localhost:3000/users");   
//     // const res = await axios.get("http://127.0.0.1:8000/User/");   --dajngo api 
//     const user = res.data.find(
//       u => u.email === form.email && u.password === form.password
//     );

//     if (user) {
//       localStorage.setItem("user", JSON.stringify(user));
//       alert("Login Successful");

//       if (user.role === "employer") {
//         navigate("/employer");
//       } else {
//         navigate("/candidate");
//       }

//     } else {
//       alert("Invalid Credentials");
//     }
//   };

//   return (
//     <div style={{padding:"20px"}}>
//       <h2>Login</h2>

//       <form onSubmit={handleLogin}>
//         <input placeholder="Email" onChange={e=>setForm({...form,email:e.target.value})} /><br/><br/>
//         <input type="password" placeholder="Password" onChange={e=>setForm({...form,password:e.target.value})} /><br/><br/>

//         <button>Login</button>
//       </form>
//     </div>
//   );
// };

// export default Login;

import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [form, setForm] = useState({
    email: "",
    password: ""
  });

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    if (!form.email || !form.password) {
      alert("Please enter email and password");
      return;
    }

    try {
      // const res = await axios.get("http://localhost:3000/users");
      const res = await axios.get("http://127.0.0.1:8000/User/");

      const user = res.data.find(
        u => u.email === form.email && u.password === form.password
      );

      if (user) {
        localStorage.setItem("user", JSON.stringify(user));

        alert("Login Successful ✅");

        if (user.role === "employer") {
          navigate("/employer");
        } else {
          navigate("/candidate");
        }

      } else {
        alert("Invalid Email or Password ❌");
      }

    } catch (error) {
      alert("Login Failed ❌");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Login</h2>

      <form onSubmit={handleLogin}>
        <input
          placeholder="Email"
          onChange={e => setForm({ ...form, email: e.target.value })}
        /><br /><br />

        <input
          type="password"
          placeholder="Password"
          onChange={e => setForm({ ...form, password: e.target.value })}
        /><br /><br />

        <button>Login</button>
      </form>
    </div>
  );
};

export default Login;