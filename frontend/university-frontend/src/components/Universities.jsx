import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/api";

function Universities() {
  const [universities, setUniversities] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    API.get("universities/")
      .then((res) => setUniversities(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="page-wrapper">
      <div className="container">
        <h2>Select University</h2>
        <div className="university-list">
          <ul>
            {universities.map((uni) => (
              <li key={uni.id}>
                <button className="apply-button" onClick={() => navigate(`/apply/${uni.id}`)} >
                  {uni.name}{" "}
                </button>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Universities;
