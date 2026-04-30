import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { http } from '@/api/axios'

export const useAuthStore = defineStore('auth', () => {
    const token = ref<string | null>(localStorage.getItem('token'))
    const user = ref<string | null>(null)

    const isAuthenticated = computed(() => !!token.value)

    async function login(username: string, password: string) {
        const response = await http.post('/token/', { username, password })
        token.value = response.data.access
        localStorage.setItem('token', response.data.access)
        await fetchUser()
    }

    async function register(username: string, password: string) {
        await http.post('/users/register/', { username, password })
        await login(username, password)
    }

    async function fetchUser() {
        const response = await http.get('/users/me/')
        user.value = response.data.username
    }

    function logout() {
        token.value = null
        user.value = null
        localStorage.removeItem('token')
    }

    return { token, user, isAuthenticated, login, register, logout, fetchUser }
})