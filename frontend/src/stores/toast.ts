import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useToastStore = defineStore('toast', () => {
    const message = ref<string | null>(null)
    let timeout: ReturnType<typeof setTimeout> | null = null

    function show(msg: string) {
        if (timeout) clearTimeout(timeout)
        message.value = msg
        timeout = setTimeout(() => {
            message.value = null
        }, 3000)
    }

    return { message, show }
})