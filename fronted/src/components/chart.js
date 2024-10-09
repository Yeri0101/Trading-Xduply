import React, { useState, useEffect } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";
import DrawingTools from "./DrawingTools"; // Importa el componente de herramientas de dibujo

function Chart() {
  const [klines, setKlines] = useState([]);

  useEffect(() => {
    // Fetch data from backend
    const fetchData = async () => {
      const response = await fetch("/api/klines");
      const data = await response.json();
      setKlines(data);
    };

    fetchData();

    // Actualiza los datos cada 5 segundos
    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <LineChart width={800} height={400} data={klines}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="close" stroke="#8884d8" />
      </LineChart>
      <DrawingTools /> {/* Renderiza las herramientas de dibujo */}
    </div>
  );
}

export default Chart;
