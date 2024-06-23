import asyncio
import visionbrowser

async def main():
    vb_folders = visionbrowser.Folders()
    token = 'YOUR_TOKEN'
    profiles = await vb_folders.get_folders_list(token=token)
    print(profiles)

if __name__ == '__main__':
    asyncio.run(main())