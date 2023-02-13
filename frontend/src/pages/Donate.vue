<template>
    <Navbar />
    <div class="container text-xl mt-10">
        <h1>Donation page</h1>
        <div>Item Name {{ name }}</div>
        <div>Item Price {{ price }}</div>
    </div>
    <Footer />
</template>

<script>
import { useRoute } from 'vue-router';
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
export default{
    name: 'Donate',
    components:{
        Navbar,
        Footer
    },
    data(){
        return{
            data: '',
            name: '',
            price: '',
        }
    },
    mounted(){
        const name = useRoute();
        this.name = name.params.name
        this.price = name.params.price
    }

}
</script>