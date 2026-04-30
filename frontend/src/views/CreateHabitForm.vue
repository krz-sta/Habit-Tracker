<script setup lang="ts">
import { ref } from 'vue';
import { useHabitStore } from '@/stores/habits';

const habitStore = useHabitStore();

const title = ref('');
const desc = ref('');
const type = ref<'good' | 'bad' | null>(null);

</script>

<template>
    <div>
        <h2>Create a habit</h2>
        <label>
            Title:<input v-model="title" />
        </label>
        <label>
            Description:<input v-model="desc" />
        </label>
        <h3>Type:</h3>
        <label>
            <input type="radio" value="good" v-model="type" />good
        </label>
        <label>
            <input type="radio" value="bad" v-model="type" />bad
        </label>

        <p v-if="type">Selected: {{ type }}</p>
    </div>
</template>
<style scoped>
</style>