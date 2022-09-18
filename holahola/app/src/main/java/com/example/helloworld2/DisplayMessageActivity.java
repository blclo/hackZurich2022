package com.example.helloworld2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

public class DisplayMessageActivity extends AppCompatActivity {
    public JSONObject json = create_json_file();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_message);

        // Get the Intent that started this activity and extract the string
        Intent intent = getIntent();
        String message = intent.getStringExtra(MainActivity.EXTRA_MESSAGE);

        // Capture the layout's TextView and set the string as its text
        TextView textView = findViewById(R.id.textView);
        // textView.setText(message);

        // open json

        try {
            json.put("floor", message);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        try {
            textView.setText(json.get("floor").toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    public JSONObject create_json_file(){
        //JSON parser object to parse read file
        String jsonStr = "{\n" +
                "      \"asyncId\": \"55f251ed70\",\n" +
                "      \"options\": {\n" +
                "          \"carSpace\": \"exclusive\",\n" +
                "          \"cars\": [\n" +
                "              {\n" +
                "                  \"building\": 1,\n" +
                "                  \"group\": 1,\n" +
                "                  \"car\": 3\n" +
                "              }\n" +
                "          ],\n" +
                "          \"destination\": {\n" +
                "              \"destinationFloor\": 0,\n" +
                "              \"destinationZone\": \"Floor 0\"\n" +
                "          }\n" +
                "      },\n" +
                "      \"target\": {\n" +
                "          \"floor\": \"3\"\n" +
                "      }\n" +
                "  }";

        // insert floor in json
        JSONObject json = null;
        try {
            json = new JSONObject(jsonStr);
            // json.put("floor", floor);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return json;
    }

    public void set_destination_floor_sch_workshop(View view) {
        TextView current_floor = findViewById(R.id.textView);
        Intent intent = new Intent(this, CallElevator.class);
        try {
            json.put("destinationFloor", "3");
            json.put("destinationZone", "Floor 3");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        startActivity(intent);
    }

    public void set_destination_floor_showers(View view) {
        TextView current_floor = findViewById(R.id.textView);
        Intent intent = new Intent(this, CallElevator.class);
        try {
            json.put("destinationFloor", "5");
            json.put("destinationZone", "Floor 5");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        startActivity(intent);
    }

    public void set_destination_floor_sleeping(View view) {
        TextView current_floor = findViewById(R.id.textView);
        Intent intent = new Intent(this, CallElevator.class);
        try {
            json.put("destinationFloor", "2");
            json.put("destinationZone", "Floor 2");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        intent.putExtra("json", json.toString());
        startActivity(intent);
    }
}