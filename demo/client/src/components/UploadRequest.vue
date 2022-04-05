<template>
    <div class="file-input" v-if="result == null">
        <h4>Try a Random Acts of Pizza request :</h4>
        <form v-on:submit.prevent="submitForm">
            <input type="text" class="w-100 my-2" name="title" placeholder="[REQUEST] Title" v-model="form.title">
            <textarea ref="requestarea" class="w-100 my-2" name="text" rows="4" cols="50" placeholder="Request content" v-model="form.text">
            </textarea>
            <div class="form-group">
                <label>Request number of 👍</label>
                <input type="number" class="w-10 m-2" name="title" min="0" placeholder="0" v-model="form.num_upvotes">
            </div>
            <div class="form-group">
                <label>Request number of 👎</label>
                <input type="number" class="w-10 m-2" name="title" min="0" placeholder="0" v-model="form.num_downvotes">
            </div>
            <div class="form-group">
                <label>Request number of comments</label>
                <input type="number" class="w-10 m-2" name="title" min="0" placeholder="0" v-model="form.num_comments">
            </div>
            <input class="btn btn-secondary" type="submit" value="Submit">
        </form>
    </div>
    <div class="result" v-else>
        <p class="result-text">Likely to receive a pizza : {{ result }}</p>
        <div>
            <button class="btn btn-secondary" @click="restart">Recommencer</button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'UploadRequest',
        data () {
            return {
                baseUrl: process.env.BASE_URL,
                form: {
                    title: '',
                    text: '',
                    num_upvotes: 0,
                    num_downvotes: 0,
                    num_comments: 0
                },
                result: null,
            }
        },
        methods: {
            submitForm() {
                if(!this.form.text){
                    alert('Please add request text')
                    return
                }

                axios.post('/upload', this.form)
                    .then(res => {
                        this.result = res.data.label
                        // console.log(process.env.BASE_URL + "temp/" + this.result)
                    })
                    .catch((err) => console.log(err));
            },
            restart() {
                window.location.reload();
            }
        }
    }
</script>

<style scoped>
    form {
        width: 50%;
        margin: auto;
    }

</style>
