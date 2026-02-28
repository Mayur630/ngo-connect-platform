import React, { useState } from "react";
import { Link } from "react-router-dom";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {
    fetch("http://127.0.0.1:8000/api/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        password,
      }),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Invalid credentials");
        }

        return res.json();
      })
      .then((data) => {
        localStorage.setItem("user", JSON.stringify(data));
        onLogin(data);
        window.location.href = "/dashboard";
      })
      .catch(() => alert("Invalid credentials"));
  };

  return (
    <section className="auth-container">
      <div className="auth-box">
        <p className="auth-kicker">Welcome Back</p>
        <h2>Login To Continue</h2>

        <input
          type="text"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={handleLogin}>Login</button>

        <p className="auth-switch">
          No account yet? <Link to="/register">Create one</Link>
        </p>
      </div>
    </section>
  );
}

export default Login;
