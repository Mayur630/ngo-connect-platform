import React, { useEffect, useState } from "react";

function DonorDashboard() {
  const [donations, setDonations] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/my-donations/", {
      credentials: "include",
    })
      .then((res) => res.json())
      .then((data) => {
        setDonations(data);
      })
      .catch(() => {
        setDonations([]);
      });
  }, []);

  const total = donations.reduce((sum, donation) => sum + donation.amount, 0);

  return (
    <section className="dashboard-shell">
      <div className="section-head align-left">
        <h2>My Donations</h2>
        <p>Review your giving history and total contribution impact.</p>
      </div>

      <div className="dashboard-total-card">Total Donated: INR {Number(total).toLocaleString("en-IN")}</div>

      <div className="dashboard-list">
        {donations.length === 0 && <p className="empty-state">No donations yet.</p>}

        {donations.map((donation) => (
          <article key={donation.id} className="dashboard-item">
            <h4>{donation.campaign_title}</h4>
            <p>INR {Number(donation.amount).toLocaleString("en-IN")}</p>
          </article>
        ))}
      </div>
    </section>
  );
}

export default DonorDashboard;
