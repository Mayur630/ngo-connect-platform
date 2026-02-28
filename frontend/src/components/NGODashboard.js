import React, { useEffect, useState } from "react";

function NGODashboard() {
  const [campaigns, setCampaigns] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/campaigns/")
      .then((res) => res.json())
      .then((data) => {
        setCampaigns(data);
      })
      .catch(() => {
        setCampaigns([]);
      });
  }, []);

  return (
    <section className="dashboard-shell">
      <div className="section-head align-left">
        <h2>My Campaigns</h2>
        <p>Track current campaign performance and total raised amounts.</p>
      </div>

      <div className="dashboard-list">
        {campaigns.length === 0 && <p className="empty-state">No campaigns yet.</p>}

        {campaigns.map((campaign) => (
          <article key={campaign.id} className="dashboard-item">
            <h4>{campaign.title}</h4>
            <p>Raised INR {Number(campaign.raised_amount || 0).toLocaleString("en-IN")}</p>
          </article>
        ))}
      </div>
    </section>
  );
}

export default NGODashboard;
