import { useState, useEffect } from "react";
import axios from "axios";

const Employer = () => {
  const [jobs, setJobs] = useState([]);
  const [applications, setApplications] = useState([]);
  const [form, setForm] = useState({
    company: "",
    post: ""
  });

  const fetchJobs = async () => {
    // const res = await axios.get("http://localhost:3000/jobs");
    const res = await axios.get("http://127.0.0.1:8000/Job/");
    setJobs(res.data);
  };

  const fetchApplications = async () => {
    // const res = await axios.get("http://localhost:3000/applications");
    const res = await axios.get("http://127.0.0.1:8000/Application/");
    setApplications(res.data);
  };

  useEffect(() => {
    fetchJobs();
    fetchApplications();
  }, []);

  const addJob = async () => {
    // await axios.post("http://localhost:3000/jobs", form);
    await axios.post("http://127.0.0.1:8000/Job/", form);
    alert("Job Added Successfully");
    fetchJobs();
  };

  const deleteJob = async (id) => {
    // await axios.delete(`http://localhost:3000/jobs/${id}`);
    await axios.delete(`http://127.0.0.1:8000/Job/${id}/`);
    fetchJobs();
  };

  return (
    <div style={{padding:"20px"}}>
      <h2>Employer Dashboard</h2>

      <h3>Add Job</h3>
      <input placeholder="Company" onChange={e=>setForm({...form,company:e.target.value})} />
      <input placeholder="Post" onChange={e=>setForm({...form,post:e.target.value})} />
      <button onClick={addJob}>Add Job</button>

      <h3>Jobs</h3>
      {jobs.map(job => (
        <div key={job.id}>
          {job.company} - {job.post}
          <button onClick={()=>deleteJob(job.id)}>Delete</button>
        </div>
      ))}

      <h3>Applications</h3>
      <table border="1">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Contact</th>
            <th>Age</th>
            <th>Resume</th>
            <th>Job</th>
          </tr>
        </thead>
        <tbody>
          {applications.map(app => (
            <tr key={app.id}>
              <td>{app.name}</td>
              <td>{app.email}</td>
              <td>{app.contact}</td>
              <td>{app.age}</td>
              <td>{app.resume}</td>
              <td>{app.company} - {app.post}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Employer;