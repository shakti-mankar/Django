import API from "./axios";

export const getJobs = () => API.get("/jobs/");
export const createJob = (data) => API.post("/jobs/", data);
export const applyJob = (jobId) => API.post("/apply/", { job: jobId });