import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import ProtectedRoute from "./components/ProtectedRoute";
import Navbar from "./components/Navbar";

import Signup         from "./pages/Signup";
import Login          from "./pages/Login";
import Dashboard      from "./pages/Dashboard";
import Checkout       from "./pages/Checkout";
import PaymentSuccess from "./pages/PaymentSuccess";
import PaymentFailure from "./pages/PaymentFailure";

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
        <Routes>
          {/* Public */}
          <Route path="/signup" element={<Signup />} />
          <Route path="/login"  element={<Login />} />

          {/* Protected */}
          <Route path="/dashboard" element={
            <ProtectedRoute><Dashboard /></ProtectedRoute>
          }/>
          <Route path="/checkout" element={
            <ProtectedRoute><Checkout /></ProtectedRoute>
          }/>
          <Route path="/payment-success" element={
            <ProtectedRoute><PaymentSuccess /></ProtectedRoute>
          }/>
          <Route path="/payment-failure" element={
            <ProtectedRoute><PaymentFailure /></ProtectedRoute>
          }/>

          {/* Default */}
          <Route path="*" element={<Navigate to="/login" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;