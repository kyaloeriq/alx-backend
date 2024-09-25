// Import the Redis client and promisify from util
import { createClient } from 'redis';
import { promisify } from 'util';

// Create the Redis client
const client = createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
  
  // Execute Redis operations
  (async () => {
    try {
      await displaySchoolValue('Holberton');
      await setNewSchool('HolbertonSanFrancisco', '100');
      await displaySchoolValue('HolbertonSanFrancisco');
    } catch (error) {
      console.error(`Error: ${error.message}`);
    } finally {
      client.quit();  // Close the client once done
    }
  })();
});

// Event listener for connection error
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Function to set a new value in Redis for a given school name.
 * @param {string} schoolName - The key to store.
 * @param {string} value - The value to associate with the key.
 * @returns {Promise<void>}
 */
function setNewSchool(schoolName, value) {
  return new Promise((resolve, reject) => {
    client.set(schoolName, value, (err, reply) => {
      if (err) {
        reject(err);
      } else {
        console.log(`Reply: ${reply}`);
        resolve();
      }
    });
  });
}

/**
 * Function to get and display the value of a given school name using async/await.
 * @param {string} schoolName - The key to retrieve from Redis.
 * @returns {Promise<void>}
 */
async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);  // Promisify the client.get function
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
  }
}
