import { useState, useEffect, createContext } from "react";
import { useAsyncError, useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
import { API_BACKEND_URL } from "../config";
import jwt_decode from "jwt-decode";

const AuthContext = createContext();
export default AuthContext;

export const AuthProvider = ({ children }) => {
  const navigate = useNavigate();
  const [suggestionQuest, setSuggestionQuest] = useState([]);
  const [userDetails, setUserDetails] = useState([]);
  const [managerDetails, setManagerDetails] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isCommunityManager, setCommunityManager] = useState(false);

  const registerUser = async (
    firstame,
    lastName,
    email,
    password,
    role,
    dob,
    about
  ) => {
    const registerData = {
      firstame,
      lastName,
      email,
      password,
      role,
      dob,
      about,
    };

    const response = await fetch(`${API_BACKEND_URL}/signup`, {
      method: "POST",
      body: JSON.stringify(registerData),
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (response.status === 201) {
      navigate("/login");
      return response;
    } else {
      throw response.statusText;
    }
  };

  const suggestionQuestFunc = async (email) => {
    const response = await fetch(
      `${API_BACKEND_URL}/api/quest/suggestion?email=${email}`,
      {
        method: "POST",
        body: "",
        header: {
          "Content-Type": "application/json",
        },
      }
    );

    const questData = await response.json();
    if (response.status === 200) {
      // console.log(questData);
      setSuggestionQuest(questData);
    } else {
      throw response.statusText;
    }
  };

  const getDetailFunc = async (userId) => {
    const response = await fetch(
      `${API_BACKEND_URL}/api/auth/user-details?user_id=${userId}`,
      {
        method: "POST",
        body: "",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    const userDetailData = await response.json();
    if (response.status === 200) {
      setUserDetails(userDetailData.user);
    } else {
      throw response.statusText;
    }
  };

  const loginUser = async (email, password) => {
    const loginData = {
      email,
      password,
    };

    const response = await fetch(`${API_BACKEND_URL}/api/auth/login`, {
      method: "POST",
      body: JSON.stringify(loginData),
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();
    if (response.status === 200) {
      setAuthTokens(data);
      const jwt_decode_data = jwt_decode(data.access_token);
      setUser(jwt_decode_data);
      localStorage.setItem("authTokens", JSON.stringify(data));

      new Promise((resolve, reject) => {
        suggestionQuestFunc(email)
          .then((res) => {
            resolve(res);
          })
          .catch((err) => reject(err));
      });

      new Promise((resolve, reject) => {
        getDetailFunc(jwt_decode_data.sub.split(":")[0])
          .then((res) => {
            resolve(res);
            navigate("./dashboard");
          })
          .catch((err) => reject(err));
      });
      return response;
    } else {
      toast.error(data.detail);
      throw response.statusText;
    }
  };

  const logoutUser = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authTokens");
    navigate("/login");
    toast.success("Logged out successfully!");
  };

  const registerManager = async (
    name,
    email,
    city,
    phone,
    password,
    passwordConfirm
  ) => {
    const registerData = {
      name,
      email,
      city,
      phone,
      password,
      passwordConfirm,
    };

    const response = await fetch(
      `${API_BACKEND_URL}/api/auth/community-manager`,
      {
        method: "POST",
        body: JSON.stringify(registerData),
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    if (response.status === 201) {
      navigate("/login-manager");
      return response;
    } else {
      throw response.statusText;
    }
  };

  const getManagerDetailFunc = async (managerId) => {
    const response = await fetch(
      `${API_BACKEND_URL}/api/auth/manager-details?manager_id=${managerId}`,
      {
        method: "POST",
        body: "",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    const userDetailData = await response.json();
    if (response.status === 200) {
      setManagerDetails(userDetailData.user);
    } else {
      throw response.statusText;
    }
  };

  const loginManager = async (email, password) => {
    const loginData = {
      email,
      password,
    };

    const response = await fetch(`${API_BACKEND_URL}/api/auth/manager-login`, {
      method: "POST",
      body: JSON.stringify(loginData),
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();
    if (response.status === 200) {
      setAuthTokens(data);
      const jwt_decode_data = jwt_decode(data.access_token);
      setUser(jwt_decode_data);
      localStorage.setItem("authTokens", JSON.stringify(data));
      setCommunityManager(true);

      new Promise((resolve, reject) => {
        getManagerDetailFunc(jwt_decode_data.sub.split(":")[0])
          .then((res) => {
            resolve(res);
            navigate("./dashboard");
          })
          .catch((err) => reject(err));
      });
      return response;
    } else {
      toast.error(data.detail);
      throw response.statusText;
    }
  };

  useEffect(() => {
    const decodeTokens = async () => {
      try {
        if (authTokens) {
          const jwt_decode_data = jwt_decode(authTokens.access_token);
          // console.log(jwt_decode_data)
          setUser(jwt_decode_data);
          if (isCommunityManager) {
            console.log(jwt_decode_data);
            // new Promise((resolve, reject) => {
            //   getManagerDetailFunc(jwt_decode_data.sub.split(":")[0])
            //     .then((res) => {
            //       resolve(res);
            //     })
            //     .catch((err) => reject(err));
            // });
          } else {
            new Promise((resolve, reject) => {
              suggestionQuestFunc(jwt_decode_data.sub.split(":")[1])
                .then((res) => {
                  resolve(res);
                })
                .catch((err) => reject(err));
            });
            new Promise((resolve, reject) => {
              getDetailFunc(jwt_decode_data.sub.split(":")[0])
                .then((res) => {
                  resolve(res);
                })
                .catch((err) => reject(err));
            });
          }
        }
      } catch (e) {
        console.log(e);
        toast.error("Error decoding access token");
      } finally {
        setLoading(false);
      }
    };
    decodeTokens();
  }, [authTokens, loading]);

  const authContextValue = {
    user,
    setUser,
    authTokens,
    setAuthTokens,
    registerUser,
    loginUser,
    logoutUser,
    suggestionQuest,
    userDetails,
    isCommunityManager,
    registerManager,
    loginManager,
    managerDetails,
  };
  return (
    <AuthContext.Provider value={authContextValue}>
      {loading ? null : children}
    </AuthContext.Provider>
  );
};
