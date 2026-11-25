"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [status, setStatus] = useState("Connecting...");

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/health`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("API request failed");
        }
        return response.json();
      })
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("Connection failed"));
  }, []);

  return (
    <main className="p-10">
      <h1 className="text-3xl font-bold">ContextFlow AI</h1>

      <p>Backend Status: {status}</p>
    </main>
  );
}
