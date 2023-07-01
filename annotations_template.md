# Label studio Labelling setup

```
<View>
    <Relations>
        <Relation value="relation"/>
    </Relations>
    <Labels name="label" toName="text">
        <Label value="Subject" background="orange" granularity="word"/>
        <Label value="Relation" background="green" granularity="word"/>
        <Label value="Object" background="blue" granularity="word"/>
        <Label value="Time" background="black" granularity="word"/>
        <Label value="Location" background="red" granularity="word"/>
    </Labels>
    <Text name="text" value="$text"/>

    <Header value="Provide additional tokens sepelrated by newline" />
    <TextArea name="answer" toName="text"
                showSubmitButton="true" maxSubmissions="1" editable="true"
                required="false" />
</View>
```