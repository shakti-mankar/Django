import { useEffect, useState } from "react";
import { getJobs, applyJob } from "../api/jobApi";

export default function CandidateDashboard() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    getJobs().then(res => setJobs(res.data));
  }, []);

  return (
    <div>
      <h2>Candidate Dashboard</h2>

      {jobs.map(job => (
        <div key={job.id}>
          {job.title}
          <button onClick={()=>applyJob(job.id)}>Apply</button>
        </div>
      ))}
    </div>
  );
}