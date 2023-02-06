<template>
    <h1>Campaign Donation Page</h1>
    {{ campaign_detail }}
</template>

<script>
import { useRoute } from 'vue-router';
export default{
    name: "CampaignDonation",
    data(){
        return{
            data: '',
            campaign_detail: ''
        }
    },
    mounted(){
        const name = useRoute();
        this.data = name.params.name
        this.get_campaign_donation_detail(name.params.name)
    },
    resources:{
        get_campaign_donation_detail(){
            return{
                method: '/api/method/sadbhavna_donatekart.api.campaign.get_campaign_detail',
                // method: "api/resource/Donation Campaign/${name}",
                onSuccess: (res) => {
                    console.log(res)
                    this.campaign_detail = res
                },
                onError: (error) => {
                    console.log(error)
                }
            }
        }
    },
    methods:{
        get_campaign_donation_detail(name){
            // axios.get('/api/resource/Donation Campaign',{
            //     filters: {'name': name},
            //     fields:["*"]
            // }).then((response) => {
            //     console.log(response.data)
            // })

            this.$resources.get_campaign_donation_detail.submit({
				name: name
			})
            
        }
    }
}
</script>