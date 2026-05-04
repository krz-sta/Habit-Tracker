import axios from "axios";

export const http = axios.create({
    baseURL: import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000/api'
});

http.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
})

http.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config

        if (error.response?.status === 401 && !originalRequest._retry) {
            if (originalRequest.url?.includes('/token/') || originalRequest.url?.includes('/register/')) {
                return Promise.reject(error)
            }

            originalRequest._retry = true

            try {
                const { useAuthStore } = await import('@/stores/auth')
                const authStore = useAuthStore()
                await authStore.refreshToken()

                originalRequest.headers.Authorization = `Bearer ${localStorage.getItem('token')}`
                return http(originalRequest)
            } catch {
                localStorage.removeItem('token')
                localStorage.removeItem('refresh')
                window.location.href = '/auth'
            }
        }

        return Promise.reject(error)
    }
)