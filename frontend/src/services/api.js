import apiClient from "./apiClient";

// health check
export const checkHealth = async () => {
  const res = await apiClient.get("/health");
  return res.data;
};

// predict price
export const predictPrice = async (date) => {
    try {
      const res = await apiClient.post("/predict", { date });
      return res.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

export const getGoldHistory = async () => {
  const res = await apiClient.get("/gold/history");
  return res.data;
};