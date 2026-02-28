import React from "react";

function formatCurrency(value) {
  return `INR ${Number(value || 0).toLocaleString("en-IN")}`;
}

const FALLBACK_CAMPAIGN_IMAGE =
  "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&w=1200&q=80";

function CampaignCard({ title, description, goal, raised, category, imageUrl, location }) {
  const safeGoal = Number(goal) || 0;
  const safeRaised = Number(raised) || 0;
  const progress = safeGoal > 0 ? Math.min(100, Math.round((safeRaised / safeGoal) * 100)) : 0;
  const user = JSON.parse(localStorage.getItem("user"));
  const backgroundStyle = {
    backgroundImage: `linear-gradient(120deg, rgba(32, 89, 67, 0.72), rgba(61, 143, 104, 0.65)), url("${imageUrl || FALLBACK_CAMPAIGN_IMAGE}")`,
  };

  const handleDonate = () => {
    if (!user) {
      alert("Please login to donate.");
      window.location.href = "/login";
      return;
    }

    alert("Donation Successful!");
  };

  return (
    <article className="campaign-card">
      <div className="campaign-image" style={backgroundStyle}>
        <span className="category-badge">{category}</span>
      </div>

      <div className="campaign-content">
        <h3>{title}</h3>
        <p className="campaign-desc">{description}</p>
        {location ? <p className="campaign-location">Location: {location}</p> : null}

        <div className="progress-wrapper">
          <div className="progress-bar">
            <div className="progress-fill" style={{ width: `${progress}%` }}></div>
          </div>
          <div className="progress-text">
            <span>{progress}% Funded</span>
            <span>{formatCurrency(safeRaised)}</span>
          </div>
          <p className="campaign-goal">Goal: {formatCurrency(safeGoal)}</p>
        </div>

        <button className="donate-btn" onClick={handleDonate}>
          Donate Now
        </button>
      </div>
    </article>
  );
}

export default CampaignCard;
