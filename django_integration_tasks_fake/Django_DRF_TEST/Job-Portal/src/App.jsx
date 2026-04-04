import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import EmployerDashboard from "./pages/EmployerDashboard";
import CandidateDashboard from "./pages/CandidateDashboard";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  return (
    <Routes>
      <Route
  path="/"
  element={
    localStorage.getItem("token")
      ? <Navigate to="/candidate" />
      : <Navigate to="/login" />
  }
/>

      <Route path="/login" element={<Login />} />

      <Route
        path="/employer"
        element={
          <ProtectedRoute>
            <EmployerDashboard />
          </ProtectedRoute>
        }
      />

      <Route
        path="/candidate"
        element={
          <ProtectedRoute>
            <CandidateDashboard />
          </ProtectedRoute>
        }
      />
    </Routes>
  );
}

export default App;