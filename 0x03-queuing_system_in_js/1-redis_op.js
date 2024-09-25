// Import the Redis client
import { createClient } from 'redis';

// Create the Redis client
const client = createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Perform Redis operations
  displaySchoolValue('Holberton', () => {
    setNewSchool('HolbertonSanFrancisco', '100', () => {
      displaySchoolValue('HolbertonSanFrancisco', () => {
        // Close the client once all operations are done
        client.quit();
      });
    });
  });
});

// Event listener for connection error
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Function to set a new value in Redis for a given school name.
 * @param {string} schoolName - The key to store.
 * @param {string} value - The value to associate with the key.
 * @param {function} callback - The callback function to execute after setting the value.
 */
function setNewSchool(schoolName, value, callback) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error: ${err.message}`);
      return;
    }
    console.log(`Reply: ${reply}`);
    callback();  // Execute the callback after setting the value
  });
}

/**
 * Function to get and display the value of a given school name.
 * @param {string} schoolName - The key to retrieve from Redis.
 * @param {function} callback - The callback function to execute after retrieving the value.
 */
function displaySchoolValue(schoolName, callback) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(reply);
    callback();  // Execute the callback after getting the value
  });
}
