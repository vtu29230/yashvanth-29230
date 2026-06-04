package com.wsms;

import org.springframework.stereotype.Service;

import java.net.HttpURLConnection;
import java.net.URL;

@Service
public class MonitorService {

    public String checkWebsite(String urlStr) {
        try {
            long start = System.currentTimeMillis();

            URL url = new URL(urlStr);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setConnectTimeout(5000);
            connection.setReadTimeout(5000);

            connection.connect();

            int responseCode = connection.getResponseCode();

            long end = System.currentTimeMillis();
            long responseTime = end - start;

            if (responseCode == 200) {
                return "UP | " + responseTime + " ms";
            } else {
                return "DOWN | Code: " + responseCode;
            }

        } catch (Exception e) {
            return "DOWN | ERROR";
        }
    }
}
