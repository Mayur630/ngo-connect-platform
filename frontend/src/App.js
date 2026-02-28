import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, NavLink, Link } from "react-router-dom";

import Login from "./components/Login";
import Register from "./components/Register";
import Campaigns from "./components/Campaigns";
import DonorDashboard from "./components/DonorDashboard";
import NGODashboard from "./components/NGODashboard";

import "./App.css";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const storedUser = localStorage.getItem("user");
    if (storedUser) setUser(JSON.parse(storedUser));
  }, []);

  const handleLogin = (userData) => {
    setUser(userData);
  };

  const handleLogout = () => {
    localStorage.removeItem("user");
    setUser(null);
  };

  return (
    <Router>
      <div className="app-shell">
        <Navbar user={user} onLogout={handleLogout} />

        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/campaigns" element={<Campaigns />} />
            <Route path="/login" element={<Login onLogin={handleLogin} />} />
            <Route path="/register" element={<Register />} />
            <Route path="/dashboard" element={<Dashboard user={user} />} />
          </Routes>
        </main>

        <Footer />
      </div>
    </Router>
  );
}

function Navbar({ user, onLogout }) {
  return (
    <header className="navbar-wrap">
      <nav className="navbar">
        <Link to="/" className="brand">
          <span className="brand-title">NGO Connect</span>
          <span className="brand-subtitle">Transparent Giving Platform</span>
        </Link>

        <div className="nav-links">
          <NavLink to="/" className={({ isActive }) => (isActive ? "active" : "")}>Home</NavLink>
          <NavLink to="/campaigns" className={({ isActive }) => (isActive ? "active" : "")}>Campaigns</NavLink>

          {user ? (
            <>
              <NavLink to="/dashboard" className={({ isActive }) => (isActive ? "active" : "")}>Dashboard</NavLink>
              <button className="nav-logout-btn" onClick={onLogout}>Logout</button>
            </>
          ) : (
            <>
              <NavLink to="/login" className={({ isActive }) => (isActive ? "active" : "")}>Login</NavLink>
              <NavLink to="/register" className={({ isActive }) => (isActive ? "active" : "")}>Register</NavLink>
            </>
          )}
        </div>
      </nav>
    </header>
  );
}

function Home() {
  const [stats, setStats] = useState({
    total_campaigns: 0,
    total_ngos: 0,
    total_donations: 0,
  });

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/stats/")
      .then((res) => res.json())
      .then((data) => setStats(data))
      .catch(() => {
        setStats({
          total_campaigns: 0,
          total_ngos: 0,
          total_donations: 0,
        });
      });
  }, []);

  return (
    <div className="home-page">
      <section className="hero">
        <div className="hero-content">
          <p className="hero-kicker">Support Verified Causes</p>
          <h1>Build Real Impact Through Trusted NGOs</h1>
          <p className="hero-lead">
            Donate confidently, discover transparent campaigns, and follow outcomes with clarity.
          </p>

          <div className="hero-actions">
            <Link to="/campaigns" className="hero-btn primary">Explore Campaigns</Link>
            <Link to="/register" className="hero-btn secondary">Join As Donor</Link>
          </div>
        </div>
      </section>

      <section className="stats-section">
        <div className="section-head">
          <h2>Platform Snapshot</h2>
          <p>Track active campaigns, partnered NGOs, and total donation activity in one place.</p>
        </div>

        <div className="stats-grid">
          <Link to="/campaigns" className="stat-card clickable">
            <h3>{stats.total_campaigns}</h3>
            <p>Active Campaigns</p>
          </Link>

          <Link to="/campaigns" className="stat-card clickable">
            <h3>{stats.total_ngos}</h3>
            <p>Partner NGOs</p>
          </Link>

          <Link to="/campaigns" className="stat-card clickable">
            <h3>{stats.total_donations}</h3>
            <p>Donation Records</p>
          </Link>
        </div>
      </section>
    </div>
  );
}

function Dashboard({ user }) {
  if (!user) {
    return <div className="dashboard-shell">Please login to continue.</div>;
  }

  if (user.role === "donor") return <DonorDashboard />;
  if (user.role === "ngo") return <NGODashboard />;

  return <div className="dashboard-shell">Welcome {user.username}</div>;
}

function Footer() {
  return (
    <footer className="footer">
      <p>Copyright 2026 NGO Connect. Final Year Engineering Project.</p>
    </footer>
  );
}

export default App;
