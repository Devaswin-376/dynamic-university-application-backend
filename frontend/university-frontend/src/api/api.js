import axios from "axios";

const API = axios.create({
  /* Base URL */
  baseURL: "http://127.0.0.1:8000/api/",
});

export default API;
