import { useState, useEffect } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

const Apply = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [job, setJob] = useState({});
  const [form, setForm] = useState({
    name: "",
    email: "",
    contact: "",
    age: "",
    resume: ""
  });

  useEffect(() => {
    // axios.get(`http://localhost:3000/jobs/${id}`)
    axios.get(`http://127.0.0.1:8000/Job/${id}/`)
      .then(res => setJob(res.data));
  }, [id]);

  const submitApplication = async () => {
    // await axios.post("http://localhost:3000/applications", {
    await axios.post("http://127.0.0.1:8000/Application/", {
      ...form,
      company: job.company,
      post: job.post
    });

    alert("Application Submitted Successfully");
    navigate("/candidate");
  };

  return (
    <div style={{padding:"20px"}}>
      <h2>Apply for Job</h2>

      <h3>{job.company} - {job.post}</h3>

      <input placeholder="Name" onChange={e=>setForm({...form,name:e.target.value})} /><br/><br/>
      <input placeholder="Email" onChange={e=>setForm({...form,email:e.target.value})} /><br/><br/>
      <input placeholder="Contact" onChange={e=>setForm({...form,contact:e.target.value})} /><br/><br/>
      <input placeholder="Age" onChange={e=>setForm({...form,age:e.target.value})} /><br/><br/>
      <input placeholder="Resume Link" onChange={e=>setForm({...form,resume:e.target.value})} /><br/><br/>

      <button onClick={submitApplication}>Submit</button>
    </div>
  );
};

export default Apply;