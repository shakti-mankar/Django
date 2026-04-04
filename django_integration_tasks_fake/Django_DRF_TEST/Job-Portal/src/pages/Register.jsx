import { useState } from "react";
import { registerUser } from "../services/authService";

const Register = () => {
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: "",
    role: "candidate", 
  });

  const handleSubmit = async () => {
    try {
      const res = await registerUser(form);
      console.log(res.data);

      alert("Registered Successfully");
    } catch (error) {
      console.error(error.response?.data);
      alert("Registration Failed");
    }
  };

  return (
    <div>
      <h2>Register</h2>

      <input
        placeholder="Username"
        onChange={(e) =>
          setForm({ ...form, username: e.target.value })
        }
      />

      <input
        placeholder="Email"
        onChange={(e) =>
          setForm({ ...form, email: e.target.value })
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) =>
          setForm({ ...form, password: e.target.value })
        }
      />

    
      <select
        onChange={(e) =>
          setForm({ ...form, role: e.target.value })
        }
      >
        <option value="candidate">Candidate</option>
        <option value="employer">Employer</option>
      </select>

      <button onClick={handleSubmit}>Register</button>
    </div>
  );
};

export default Register;