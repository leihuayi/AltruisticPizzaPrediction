<template>
    <div class="file-input" v-if="result == null">
        <h4>Try a Random Acts of Pizza request :</h4>
        <form v-on:submit.prevent="submitForm">
            <textarea ref="requestarea" name="text" rows="4" cols="50" placeholder="[REQUEST]" v-model="form.text">
            </textarea><br>
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
                form: {text: ''},
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


</style>
