// Function to fetch data from the API
async function fetchData() {
    try {
        const response = await fetch('http://127.0.0.1:8000/council_list.json');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Function to render data in cards
async function renderData() {
    const container = document.querySelector('.new_container');
    const data = await fetchData();

    if (!data) {
        return;
    }

    data.forEach(item => {
        const card = document.createElement('div');
        card.classList.add('card');

        const image = document.createElement('img');
        const name = document.createElement('h2');
        const role = document.createElement('h3');
        const pronoun = document.createElement('h3');
        const email = document.createElement('h3');
        const bio = document.createElement('p');

        image.src = item.profilepic;
        name.textContent = item.firstname + " " + item.lastname;
        role.textContent = item.role;
        pronoun.textContent = item.pronouns;
        email.textContent = item.email;
        bio.textContent = item.bio;

        card.appendChild(image);
        card.appendChild(name);
        card.appendChild(role);
        card.appendChild(pronoun);
        card.appendChild(email);
        card.appendChild(bio);

        container.appendChild(card);
    });
}

// Call the renderData function to display data
renderData();