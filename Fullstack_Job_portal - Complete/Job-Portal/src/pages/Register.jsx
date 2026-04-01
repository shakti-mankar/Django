// import { useState } from "react";
// import axios from "axios";
// import { useNavigate } from "react-router-dom";

// const Register = () => {
//   const [form, setForm] = useState({
//     name: "",
//     email: "",
//     password: "",
//     role: "candidate"
//   });

//   const navigate = useNavigate();

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     await axios.post("http://localhost:3000/users", form);
//     // await axios.post("http://127.0.0.1:8000/User/", form);   -- django api
//     alert("Registered Successfully");
//     navigate("/login");
//   };

//   return (
//     <div style={{padding:"20px"}}>
//       <h2>Register</h2>
//       <form onSubmit={handleSubmit}>
//         <input placeholder="Name" onChange={e=>setForm({...form,name:e.target.value})} /><br/><br/>
//         <input placeholder="Email" onChange={e=>setForm({...form,email:e.target.value})} /><br/><br/>
//         <input type="password" placeholder="Password" onChange={e=>setForm({...form,password:e.target.value})} /><br/><br/>

//         <select onChange={e=>setForm({...form,role:e.target.value})}>
//           <option value="candidate">Candidate</option>
//           <option value="employer">Employer</option>
//         </select><br/><br/>

//         <button>Register</button>
//       </form>
//     </div>
//   );
// };

// export default Register;

import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    role: "candidate"
  });

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!form.name || !form.email || !form.password) {
      alert("Please fill all fields");
      return;
    }

    try {
      // const res = await axios.get("http://localhost:3000/users");
      const res = await axios.get("http://127.0.0.1:8000/User/");

      const exists = res.data.find(u => u.email === form.email);

      if (exists) {
        alert("User already exists ❌");
        return;
      }

      // await axios.post("http://localhost:3000/users", form);
      await axios.post("http://127.0.0.1:8000/User/", form);

      alert("Registered Successfully ✅");
      navigate("/login");

    } catch (error) {
      alert("Registration Failed ❌");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Register</h2>

      <form onSubmit={handleSubmit}>
        <input placeholder="Name"
          onChange={e => setForm({ ...form, name: e.target.value })} /><br /><br />

        <input placeholder="Email"
          onChange={e => setForm({ ...form, email: e.target.value })} /><br /><br />

        <input type="password" placeholder="Password"
          onChange={e => setForm({ ...form, password: e.target.value })} /><br /><br />

        <select
          onChange={e => setForm({ ...form, role: e.target.value })}
        >
          <option value="candidate">Candidate</option>
          <option value="employer">Employer</option>
        </select><br /><br />

        <button>Register</button>
      </form>
    </div>
  );
};

export default Register;