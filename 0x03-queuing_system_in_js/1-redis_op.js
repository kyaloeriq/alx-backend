// Import the Redis client
import { createClient } from 'redis';

// Create the Redis client
const client = createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Call the functions after connection is established
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});

// Event listener for connection error
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Function to set a new value in Redis for a given school name.
 * @param {string} schoolName - The key to store.
 * @param {string} value - The value to associate with the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error: ${err.message}`);
      return;
    }
    console.log(`Reply: ${reply}`);
  });
}

/**
 * Function to get and display the value of a given school name.
 * @param {string} schoolName - The key to retrieve from Redis.
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(reply);
  });
}

// Close the client after a short delay to ensure all commands are completed
setTimeout(() => {
  client.quit();
}, 1000);
