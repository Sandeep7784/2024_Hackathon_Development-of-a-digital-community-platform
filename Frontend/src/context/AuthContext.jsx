import { createContext, useEffect, useState } from "react";
import { jwtDecode } from 'jwt-decode';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    // slower puts extra load on the browser
    // const [user, setUser] = useState(localStorage.getItem('authTokens') ? jwtDecode(localStorage.getItem('authTokens')) : null);
    // const [authTokens, setAuthTokens] = useState(localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null);

    // faster as compare to the above one
    let [authTokens, setAuthTokens] = useState(()=> localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
    let [user, setUser] = useState(()=> localStorage.getItem('authTokens') ? jwtDecode(localStorage.getItem('authTokens')) : null)
    let [loading, setLoading] = useState(true);

    const navigate = useNavigate();

    const loginUser = async (e) => {
        e.preventDefault();
        let response = await fetch('http://127.0.0.1:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'username': e.target.email.value, 'password': e.target.password.value}) 
        })
        let data = await response.json();
        // console.log("data", data);
        if (response.status === 200) {
            setAuthTokens(data);
            let decoded = jwtDecode(data.access);
            setUser(decoded);
            // console.log(decoded);
            localStorage.setItem('authTokens', JSON.stringify(data));
            navigate('/');
        } else {
            alert('Something went wrong. Please try again.')
        }
    }

    const logoutUser = () => {
        setAuthTokens(null);
        setUser(null);
        localStorage.removeItem('authTokens');
        navigate('/login');
    }

    const updateToken = async () => {
        // console.log("ho bc gya update");
        let response = await fetch('http://127.0.0.1:8000/api/token/refresh', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'refresh': authTokens.refresh}) 
        })
        let data = await response.json();
        if (response.status === 200) {
            setAuthTokens(data);
            let decoded = jwtDecode(data.access);
            setUser(decoded);
            localStorage.setItem('authTokens', JSON.stringify(data));
        } else {
            logoutUser();
        }
    }

    const contextData = {
        user: user,
        loginUser: loginUser,
        logoutUser: logoutUser,
    };

    useEffect(() => {
        const fourMinutes = 1000 * 60 * 4;
        let interval = setInterval(() => {
            if (authTokens) {
                updateToken();
            }            
        }, fourMinutes);
        return () => clearInterval(interval);

    }, [authTokens, loading]);

    return (
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthContext;