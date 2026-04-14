import apiClient from "./apiClient";

// health check
export const checkHealth = async () => {
  const res = await apiClient.get("/health");
  return res.data;
};

// predict price
export const predictPrice = async (year, usdRate) => {
  const response = await apiClient.post("/predict", {
    year: Number(year),
    usd_to_inr: Number(usdRate)
  });
  return response.data;
};

export const getGoldHistory = async () => {
  const res = await apiClient.get("/gold/history");
  return res.data;
};