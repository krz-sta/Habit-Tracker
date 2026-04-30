<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const username = ref('')
const password = ref('')
const error = ref<string | null>(null)

async function handleRegister() {
    error.value = null
    try {
        await authStore.register(username.value, password.value)
        router.push('/')
    } catch (e: any) {
        error.value = e.response?.data?.detail ?? 'Register failed.'
    }
}
</script>

<template>
    <div>
        <h1>Register</h1>
        <input v-model="username" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button @click="handleRegister">Register</button>
        <p v-if="error">{{ error }}</p>
    </div>
</template>
<style scoped>
</style>