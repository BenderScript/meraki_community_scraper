
# How to Scrape a Forum for Awesome GPT Fine-Tuning Data

Welcome to this repository, where you will learn how to scrape a community forum for some amazing data that you can use to fine-tune your chatGPT model. This is a cool project that shows you how to build an AI solution from scratch, from data collection to model deployment.

This is the first part in a series of a complete fine-tuning example from scratch. The second part is here: https://github.com/BenderScript/techGPT

## Scraping and Cleaning Data

Before we get to the fun part of GenAI, we need to get some data first. And not just any data, but high-quality data that is relevant and useful for our task.

Scraping a forum is not as easy as it sounds. There are many challenges and decisions that we need to face, such as:

- How do we extract the questions and answers from the HTML structure of the forum pages?
- How do we deal with the pagination of the forum pages? Do we scrape all the pages or just the first few?
- How do we select the best answers for each question? Do we only consider the accepted solutions, or do we also include the ones with many upvotes?
- How do we deal with grammar and spelling errors in the text? Do we correct them or leave them as they are?
- How do we handle code snippets, links, emails, HTML tags, emojis, and special characters in the text? Do we remove them or keep them? And if we keep them, how do we format them properly?

As you can see, there are many things to think about before we can start scraping the data.

## Rewriting the Questions and Answers 

Once we have scraped and cleaned the data, we need to prepare it for training. This means that we need to transform the data into a format that GenAI can understand. In other words, we need to rephrase the questions and answers in a way that preserves their meaning and tone.

For example, a question like: " I tried configuring a new wireless AP and I need to know how to configure the SSID and the password. Can someone help me? "
needs to be rephrased as: "How do I set up the SSID and password on a new wireless AP?"

The same goes for the answers. We need to rephrase them in a clear and concise way.

The approach that I used in this repository is to leverage chatGPT itself to clean and rephrase the questions and answers.

At first, I tried coding a complex regex expression to clean the data, but after many tests, I realized that chatGPT could do a better job.

I also found out that doing it in two steps was better. First, I asked chatGPT to clean the data, and then I asked it to rephrase it. Yes, this takes more time, but the results are worth it.

Okay, here is a possible rewritten version of that part:

## How to Run It

To make this repository work, you need **Python 3.9** or above on your computer. You also need to get the Python libraries in **requirements.txt** using pip:

You need a `.env` file with your OpenAI API key as in

```bash
OPENAI_API_KEY=<your api key>
```

To run it with the default settings, just type:

```bash
python3 main.py
```

## Examples

Examples of saved JSON Lines files

```json lines
{"messages": [{"role": "system", "content": "You are a tech support person for the Meraki product line. You can answer questions about the features, specifications, installation, configuration, and troubleshooting of the Meraki products. You are polite,professional, and helpful. You use clear and simple language and provide relevant links or resources when possible."}, {"role": "user", "content": "What could be causing the issue if the green LED is showing on all the newly added MR44 devices but they are not being displayed as online on the dashboard?"}, {"role": "assistant", "content": "To get all the devices online on the dashboard, please follow these steps:\n\n1. Remove the device from the current network.\n2. Create a new network.\n3. Add the device to the new network.\n4. Factory reset the device.\n5. Move the device back to the original network.\n\nFor more information, you can refer to the original post here: [Wireless-LAN/Meraki-is-showing-green-led-but-it-doesn-t-show-that-online-on](/t5/Wireless-LAN/Meraki-is-showing-green-led-but-it-doesn-t-show-that-online-on/m-p/212259#M29291)"}]}
{"messages": [{"role": "system", "content": "You are a tech support person for the Meraki product line. You can answer questions about the features, specifications, installation, configuration, and troubleshooting of the Meraki products. You are polite,professional, and helpful. You use clear and simple language and provide relevant links or resources when possible."}, {"role": "user", "content": "What could be the reason for the presence of different application categories in my networks, where one network has a more extensive drop-down list of applications compared to the other? It appears that the variation in application lists is due to the presence of MR36 models in the network with more applications, whereas the other network consists of a combination of MR33, MR36, MR52, MR44, and MR86 models. The provided image displays that the Software Updates category specifically contains only 2 categories in one network, while the other network has a greater number of options in the drop-down list for the same category. This pattern is also observed in other Application Categories."}, {"role": "assistant", "content": "To find out what happens when mixing AP models and one of them lacks support for WiFi AX/NBAR, the Meraki categories are used as a fallback for that particular network. For more details on the integration of Next-gen Traffic Analytics - Network-Based Application Recognition (NBAR), you can refer to the link provided: https://documentation.meraki.com/General_Administration/Cross-Platform_Content/Next-gen_Traffic_Analytics_-_Network-Based_Application_Recognition_(NBAR)_Integration#Wireless.\n\nTo see the solution mentioned in the original post, please visit /t5/Wireless-LAN/Meraki-Firewall-amp-traffic-shaping/m-p/211985#M29256."}]}
{"messages": [{"role": "system", "content": "You are a tech support person for the Meraki product line. You can answer questions about the features, specifications, installation, configuration, and troubleshooting of the Meraki products. You are polite,professional, and helpful. You use clear and simple language and provide relevant links or resources when possible."}, {"role": "user", "content": "How can I identify the user or device that is currently using the most bandwidth in real time on the MX400?"}, {"role": "assistant", "content": "No, I don't think so on the MX series. However, if you have the Meraki Switch/AP product, you can trace it back to the client, although it may not be useful in this situation. If you have NetFlow enabled, you can analyze the flow almost instantly with your preferred NetFlow product."}]}
{"messages": [{"role": "system", "content": "You are a tech support person for the Meraki product line. You can answer questions about the features, specifications, installation, configuration, and troubleshooting of the Meraki products. You are polite,professional, and helpful. You use clear and simple language and provide relevant links or resources when possible."}, {"role": "user", "content": "What should be considered when determining the appropriate size of the MX at the central site for deploying SSID tunneling?"}, {"role": "assistant", "content": "The reply from @Ryan_Miles (/t5/user/viewprofilepage/user-id/326) below explains that it's not just the number of clients that matter in this case. The aggregate number of WiFi users and the traffic generated by each user also affect the Wireless concentrator MX. Ryan mentions that if there are any capacity issues on the concentrator, they would likely impact all users. Therefore, it's advisable to avoid reaching its maximum capacity. To monitor usage, you can check the Org > Summary reports page, specifically focusing on the Network where the wireless concentrator MX is located. Additionally, remember that you can utilize traffic shaping on the MR access points to manage the traffic generated by your client base. You can find the original post with the solution here (/t5/Wireless-LAN/SSID-tunneling/m-p/211669#M29202)."}]}
```

## Feedback

If you think this is interesting and want to contribute or suggest better ways to go about cleaning and preparing data I am all ears!

