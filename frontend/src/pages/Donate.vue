<template>
    <h1>Donation page</h1>
    <div>{{ name }}</div>
</template>

<script>
import { useRoute } from 'vue-router';
export default{
    name: 'Donate',
    data(){
        return{
            data: '',
            name: ''
        }
    },
    mounted(){
        const name = useRoute();
        this.name = name.params.name
    }
}
</script>