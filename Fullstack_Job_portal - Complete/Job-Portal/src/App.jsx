import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";


import Register from "./pages/Register";
import Login from "./pages/Login";
import Employer from "./pages/Employer";
import Candidate from "./pages/Candidate";
import Apply from "./pages/Apply";
import Navbar from "./components/Navbar";

const ProtectedRoute = ({ children }) => {
  const user = JSON.parse(localStorage.getItem("user"));
  return user ? children : <Navigate to="/login" />;
};

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />

        <Route
          path="/employer"
          element={
            <ProtectedRoute>
              <Employer />
            </ProtectedRoute>
          }
        />

        <Route
          path="/candidate"
          element={
            <ProtectedRoute>
              <Candidate />
            </ProtectedRoute>
          }
        />

        <Route
          path="/apply/:id"
          element={
            <ProtectedRoute>
              <Apply />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;