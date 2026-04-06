import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Candidate = () => {
  const [jobs, setJobs] = useState([]);
  const navigate = useNavigate();

  const fetchJobs = async () => {
    // const res = await axios.get("http://localhost:3000/jobs");
    const res = await axios.get("http://127.0.0.1:8000/Job/");
    setJobs(res.data);
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  return (
    <div style={{padding:"20px"}}>
      <h2>Candidate Dashboard</h2>

      {jobs.map(job => (
        <div key={job.id} style={{border:"1px solid black",margin:"10px",padding:"10px"}}>
          <h3>{job.company}</h3>
          <p>{job.post}</p>
          <button onClick={()=>navigate(`/apply/${job.id}`)}>Apply</button>
        </div>
      ))}
    </div>
  );
};

export default Candidate;