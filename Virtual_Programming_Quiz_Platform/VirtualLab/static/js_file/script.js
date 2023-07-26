document.getElementById('submit').addEventListener('click', function open() {
    const values = document.getElementById('searchItem').value.toUpperCase();
    document.getElementById('searchItem').value = null;
    if (values == '777' || values == 'CHARLIE') {
        window.location.href = '/Charlie/';
    }
    else if (values == 'CHUP') {
        window.location.href = '/Chup/';

    }
    else if (values == 'FREDDY') {
        window.location.href = '/freddy/';

    }
    else if (values == 'GHOST STORY'||values == 'GHOSTSTORY') {
        window.location.href = '/ghostStory/';

    }
    else if (values == 'GOODBYE'||values == 'GOOD BYE') {
        window.location.href = '/GoodByeMovie/';

    }
    else {
        window.alert("Service Not Available");
    }
})