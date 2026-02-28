import React, { useEffect, useState } from "react";
import CampaignCard from "./CampaignCard";

function Campaigns() {
  const [campaigns, setCampaigns] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/campaigns/")
      .then((res) => res.json())
      .then((data) => setCampaigns(data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <section className="campaign-section">
      <div className="section-head">
        <h2>Active Campaigns</h2>
        <p>Support urgent initiatives from verified organizations.</p>
      </div>

      <div className="card-container">
        {campaigns.map((c) => (
          <CampaignCard
            key={c.id}
            title={c.title}
            description={c.description}
            goal={c.goal_amount}
            raised={c.raised_amount}
            category={c.category}
            imageUrl={c.image_url}
            location={c.location}
          />
        ))}
      </div>
    </section>
  );
}

export default Campaigns;
