import { useEffect, useState } from "react";
import { getJobs, createJob } from "../api/jobApi";

export default function EmployerDashboard() {
  const [jobs, setJobs] = useState([]);
  const [title, setTitle] = useState("");

  const fetchJobs = async () => {
    const res = await getJobs();
    setJobs(res.data);
  };

  const handleCreate = async () => {
    await createJob({ title, description: "Test job" });
    fetchJobs();
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  return (
    <div>
      <h2>Employer Dashboard</h2>

      <input placeholder="Job Title" onChange={(e)=>setTitle(e.target.value)} />
      <button onClick={handleCreate}>Create Job</button>

      {jobs.map(job => (
        <div key={job.id}>{job.title}</div>
      ))}
    </div>
  );
}