<template>
    <div id="create" class="row">
        <div class="col-2">
            <ReviewSidebar :movieId="id"/>
        </div>
        <div class="col-10">
            <!-- title -->
            <div id="form">
                <b-form-group class="mb-2" label="Title" label-for="title" description="Write your review for the movie">
                    <b-form-input type="text" id="title" v-model="reviewData.title"> </b-form-input>
                </b-form-group>
                <!-- rating -->
                <b-input-group class="mb-2">
                    <b-input-group-prepend><b-button id="ratingButton">Rating</b-button>   
                    </b-input-group-prepend>
                    <b-form-rating v-model="reviewData.rating" stars="10" variant="warning"></b-form-rating>
                    <b-input-group-append>
                        <b-input-group-text class="justify-content-center" style="min-width: 3em;">
                        {{ reviewData.rating }}
                        </b-input-group-text>
                    </b-input-group-append>
                </b-input-group>
                
                <!-- content -->
                <b-form-group class="mb-2" label="Content" label-for="content">
                    <b-form-textarea
                    id="content"
                    v-model="reviewData.content"
                    placeholder="Write your review content"
                    ></b-form-textarea>
                </b-form-group>
                <b-button id="submitButton" @click="onWrite">Submit</b-button> 
            </div>
        </div>
    </div>
</template>

<script>
import ReviewSidebar from '@/components/ReviewSidebar.vue'
import { mapActions } from 'vuex'
export default {
    name: 'ReviewCreate',
    components: {
        ReviewSidebar,
    },
    data() {
        return {
            reviewData: {
                title: null,
                content: null,
                rating: null
            },
            id: this.$route.params.id
        }
    },
    methods: { 
        ...mapActions(['createReview']), 
        onWrite() { 
            this.createReview({reviewData: this.reviewData, id: this.$route.params.id})
        }
    },
}
</script>

<style scoped>

#form {
    width: 80%;
    text-align: left;
    margin: 30px auto;
    
}
b-form-group {
    text-align: left;
}
#content {
    height: 300px;
}
#rating {
    width: 80%;
}
#submitButton {
    background-color: #3fb883;
    color: white;
    border: 1px solid #3fb883;
}
#submitButton:hover {
    background-color: #3baa7a;
}
#ratingButton {
    background-color: #3fb883;
    color: white;
    border: 1px solid #3fb883;
}
#ratingButton:hover {
    background-color: #3baa7a;
}

</style>