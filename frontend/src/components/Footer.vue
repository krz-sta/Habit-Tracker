<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { Github, Linkedin, Globe } from 'lucide-vue-next';

const route = useRoute();
const router = useRouter();

</script>

<template>
<footer class="bg-gray-900 text-gray-400 py-8">
    <div class="max-w-7xl mx-auto px-4 text-center flex flex-col gap-2">
        <p>2026 Habit Tracker, Made by Krzysztof Stasiak:</p>
        <div class="mx-auto flex justify-center gap-3">
            <a href="https://github.com/krz-sta" target="_blank" rel="noopener noreferrer"><Github class="hover:text-gray-300"/></a>
            <a href="https://www.linkedin.com/in/krzysztof-stasiak-503235301/" target="_blank" rel="noopener noreferrer"><Linkedin class="hover:text-gray-300"/></a>
            <a href="https://krzysztofstasiak.pl" target="_blank" rel="noopener noreferrer"><Globe class="hover:text-gray-300"/></a>
        </div>
    </div>
</footer>
</template>

<style scoped>
</style>